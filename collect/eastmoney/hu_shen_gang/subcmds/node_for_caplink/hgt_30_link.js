const puppeteer = require('puppeteer');
const TAB_HGTCG = 'http://data.eastmoney.com/hsgtcg/StockStatistics.aspx?tab=1'
const HGT_30 = '#filter_ggtj > div.cate_type > ul > li:nth-child(5) > span'
const HGT_PAGE_1 = '#PageCont > a:nth-child(2)'
const HGT_PAGE_2 = '#PageCont > a:nth-child(3)'

async function run() {
  const browser = await puppeteer.launch({headless: true});
  const page = await browser.newPage();

  // 1. 打开[沪股通]
  await page.goto(TAB_HGTCG);

  // 2. 点击[近30日]
  await page.waitFor(2000);
  await page.click(HGT_30)

  // 3. 点击[第2页]
  await page.waitFor(2000);
  await page.click(HGT_PAGE_2)

  // 等待tshark启动
  await page.waitFor(5000);
  
  // 4. 点击[第1页]
  await page.click(HGT_PAGE_1)
  await page.waitFor(2000);

  browser.close();
}
run();
