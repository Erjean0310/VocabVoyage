import mysql.connector
import csv  # 添加导入csv模块

# 数据库连接信息
db_config = {
    'host': '',
    'user': '',
    'password': '',
    'database': ''
}

try:
    # 连接到数据库
    connection = mysql.connector.connect(**db_config)
    
    if connection.is_connected():
        print("成功连接到数据库")

        # 创建游标
        cursor = connection.cursor()

        # 执行查询
        cursor.execute("SELECT * FROM words")  # 选择所有列

        # 获取所有结果
        results = cursor.fetchall()

        # 获取字段名
        field_names = [i[0] for i in cursor.description]  # 获取字段名

        # 打印结果
        for row in results:
            print(row)

        # 导出到CSV文件
        with open('output.csv', mode='w', newline='', encoding='utf-8') as file:  # 创建CSV文件
            writer = csv.writer(file)
            writer.writerow(field_names)  # 写入字段名
            writer.writerows(results)  # 写入所有行

except mysql.connector.Error as err:
    print(f"数据库连接错误: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("数据库连接已关闭")
        print("over")

