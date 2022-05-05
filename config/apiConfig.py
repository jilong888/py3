import config.commonConfig as conf
apiUrl_test20_linear='http://test20-linear-ingress.bitfanssim.com';
apiUrl_test20_contract='http://api.test-20.dm.huobiapps.com';apiUrl_test20_swap=apiUrl_test20_linear
api_path_swap='/swap-api/v1/';api_path_linear='/linear-swap-api/v1/';api_path_contract='/api/v1/';

apiUrls={
    '20':{conf.contract_flag:apiUrl_test20_contract,conf.swap_flag:apiUrl_test20_swap,conf.linear_flag:apiUrl_test20_linear}
}
api_path={conf.contract_flag:api_path_contract,conf.swap_flag:api_path_swap,conf.linear_flag:api_path_linear}