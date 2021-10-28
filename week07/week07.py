# 作者：童鼎
# 使用字典练习购物车系统


#创建商品清单
item = {
    1:['鬼泣',200],
    2:['只狼',198],
    3:['仙剑奇侠传七',128],
    4:['黑暗之魂3',168],
    5:['鬼谷八荒',68],
    6:['觅长生',88]
}

#输入用户的银行卡余额
money = input('请输入您的账户余额：')
money = int(money)
quit = 1
#添加购物清单
shopping_item = []
price = 0 #购物车内的物品价格
while True:
    # 打印商品目录
    print('info'.center(50, "-"))
    for i in range(len(item)):
        print('物品序列：%d  物品名称：%s 物品价格：%d' % (i + 1, item[i + 1][0], item[i + 1][1]))
    if price<= money:
        shopping = input('还有余额，请输入你需要购买的商品的序列号')  # 输入需要购买的商品的序列号
        shopping = int(shopping)  # 将输入序列号的数据类型由str转换为int
        shopping_item.append(shopping)  # 将购买的商品加入购物清单
        price += item[shopping][1]
        quit = input('退出请输入q,继续购物请输入任意键：')
        if price > money:
            print('余额不足，购买失败')
            print('您购买的物品序号如下：'+str(shopping))
        elif quit == 'q':
            print('本次购物已结束，本次的购物清单如下所示：')
            for it in item:
                print('您购买了')



