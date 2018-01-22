const puppeteer = require('puppeteer');
const TAB_HGTCG = 'http://data.eastmoney.com/hsgtcg/StockStatistics.aspx?tab=1'
const HGT_30 = '#filter_ggtj > div.cate_type > ul > li:nth-child(5) > span'
WAIT_TIME = 5 * 1000
async function run() {
  const browser = await puppeteer.launch({headless: false});
  const page = await browser.newPage();

  // 1. 打开[沪股通]
  await page.goto(TAB_HGTCG);

  // 等待tshark启动
  await page.waitFor(WAIT_TIME);
  
  // 2. 点击[近30日]
  await page.click(HGT_30)
  browser.close();
}
run();
