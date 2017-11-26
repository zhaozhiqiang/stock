import os
import re
import sys
import codecs
from subprocess import check_output


STOCKS = '../../data/stock_list.txt'
EASTMONEY = 'http://quote.eastmoney.com/stocklist.html'


def get_stocks_id(html):
    regex = r'http:.*.com\/((sz|sh)[0-9]+)'
    matches = re.finditer(regex, html)
    stocks_id = []
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
        stocks_id.append(match.group(1))
        #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
        #for groupNum in range(0, len(match.groups())):
        #    groupNum = groupNum + 1
        #    
        #    print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
        #print match.group(1)
    #print stocks_id
    return stocks_id


def get_html():
    # print sys.argv[1]
    if os.path.isfile(STOCKS) and ('-r' == sys.argv[1]):
        os.remove(STOCKS)
    html = check_output(['curl', EASTMONEY]).decode('gbk').encode('utf-8')
    return html


if __name__ == '__main__':
    html = get_html()
    stocks_id = get_stocks_id(html)
    #print stocks_id
    with open(STOCKS, 'w') as f:
        f.write(str(stocks_id))
