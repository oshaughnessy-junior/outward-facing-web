// Bounded rendering regression check for the isolated CI build, never production mutation.
const fs = require("node:fs");
const { Builder, By, Key } = require("selenium-webdriver");
const chrome = require("selenium-webdriver/chrome");
const routes = ["", "research/", "astrophysics/", "ai-agents/", "repositories/", "people/", "projects/"];
const output = "layout-evidence";
fs.mkdirSync(output, { recursive: true });
const report = { source: process.env.GITHUB_SHA, observedAt: new Date().toISOString(), pages: [], errors: [] };
(async () => {
  const driver = await new Builder()
    .forBrowser("chrome")
    .setChromeOptions(
      new chrome.Options().setChromeBinaryPath(process.env.AUDIT_CHROME).addArguments("--headless=new", "--no-sandbox", "--disable-dev-shm-usage")
    )
    .setChromeService(new chrome.ServiceBuilder(process.env.AUDIT_DRIVER))
    .build();
  try {
    await driver.manage().setTimeouts({ pageLoad: 30000, script: 10000 });
    for (const width of [1440, 390]) {
      await driver
        .manage()
        .window()
        .setRect({ width: Math.max(width, 500), height: 1000 });
      await driver.sendDevToolsCommand("Emulation.setDeviceMetricsOverride", { width, height: 1000, deviceScaleFactor: 1, mobile: false });
      for (const route of routes) {
        await driver.get(`http://localhost:8080/${route}`);
        await driver.wait(() => driver.executeScript('return document.readyState === "complete"'), 10000);
        const page = await driver.executeScript(() => ({
          url: location.href,
          viewport: innerWidth,
          documentWidth: document.documentElement.scrollWidth,
          h1: document.querySelectorAll("h1").length,
          mainCssLoaded: [...document.styleSheets].some((s) => s.href && /\/main\.css/.test(s.href)),
          brokenImages: [...document.images].filter((i) => i.complete && !i.naturalWidth).map((i) => i.src),
          missingAlt: [...document.images].filter((i) => !i.hasAttribute("alt")).map((i) => i.src),
        }));
        page.requestedWidth = width;
        report.pages.push(page);
        for (const [name, fail] of Object.entries({
          viewport: page.viewport !== width,
          overflow: page.documentWidth > page.viewport + 1,
          heading: page.h1 !== 1,
          stylesheet: !page.mainCssLoaded,
          images: page.brokenImages.length > 0,
          alt: page.missingAlt.length > 0,
        })) {
          if (fail) report.errors.push({ route, width, check: name });
        }
        if (route === "" || route === "research/") {
          fs.writeFileSync(`${output}/${route ? "research" : "home"}-${width}.png`, await driver.takeScreenshot(), "base64");
        }
        if (width === 390 && route === "") {
          const menu = await driver.findElement(By.css(".navbar-toggler"));
          await menu.sendKeys(Key.ENTER);
          await driver.wait(async () => (await menu.getAttribute("aria-expanded")) === "true", 3000);
          page.keyboardMenuExpanded = true;
        }
      }
    }
  } catch (error) {
    report.errors.push({ message: String(error) });
  } finally {
    fs.writeFileSync(`${output}/results.json`, JSON.stringify(report, null, 2));
    await driver.quit();
  }
  console.log(JSON.stringify({ pages: report.pages.length, errors: report.errors }));
  if (report.errors.length) process.exitCode = 1;
})().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
