import pytest
# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    args = ["--alluredir=report/allure"]
    system_types_item='行情/Test_Noti_Kline.py'
    args.append(f"testCase/{system_types_item}")
    pytest.main(args=args)
    # pytest.main()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
