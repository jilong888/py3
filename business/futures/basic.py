# 合约代码处理：btc_4转换为btc_cw,btc_nw,btc_cq,btc_nq（1:仅当周、2:当周+次周、3:当周+次周+当季、4:当周+次周+当季+次季）
# author: Brian Gene     at 2022-02-22
def symbols(contractCodeList):
    s = ''
    for i in range(contractCodeList.split(',').__len__()):
        a = 0;t = '&';contractCode = contractCodeList.split(',')[i];
        if '-' in contractCode: t = '-'  # 正向交割
        if '_' in contractCode: t = '_'  # 反向交割
        if t + '1' == contractCode[-2:]:    a = contractCodeList.find(t + '1');s = s + contractCode[:a] + 'cw' + ','
        if t + '2' == contractCode[-2:]:   a = contractCodeList.find(t + '1');s = s + contractCode[:a] + 'cw' + ',' + contractCode[:a] + 'nw' + ','
        if t + '3' == contractCode[-2:]:    a = contractCodeList.find(t + '1');s = s + contractCode[:a] + 'cw' + ',' + contractCode[:a] + 'nw' + ',' + contractCode[:a] + 'cq' + ','
        if t + '4' == contractCode[-2:]:    a = contractCodeList.find(t + '1');s = s + contractCode[:a] + 'cw' + ',' + contractCode[:a] + 'nw' + ',' + contractCode[:a] + 'cq' + ',' + contractCode[:a] + 'nq' + ','
        if t + '1' != contractCode[-2:] and t + '2' != contractCode[-2:] and t + '3' != contractCode[-2:] and t + '4' != contractCode[-2:]: s = s + contractCode + ','
    s = s[:-1]
    return s.upper()