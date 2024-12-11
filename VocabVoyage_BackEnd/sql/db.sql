-- 创建数据库
CREATE DATABASE IF NOT EXISTS vocab_voyage;
USE vocab_voyage;

-- 创建用户表
CREATE TABLE user (
                      id INT AUTO_INCREMENT PRIMARY KEY COMMENT '用户ID',
                      nick_name VARCHAR(255) COMMENT '昵称',
                      phone VARCHAR(16) UNIQUE NOT NULL COMMENT '手机号',
                      password VARCHAR(10) COMMENT '用户密码',
                      score INT DEFAULT 0 COMMENT '积分',
                      role VARCHAR(255) DEFAULT 'user' COMMENT '角色'
) COMMENT '用户表';


-- 创建单词表
CREATE TABLE word (
                      id INT PRIMARY KEY AUTO_INCREMENT COMMENT '单词ID',
                      word VARCHAR(255) NOT NULL COMMENT '单词',
                      meaning VARCHAR(255) COMMENT '单词含义',
                      description VARCHAR(1024) COMMENT '单词描述'
) COMMENT '单词表';

-- 创建记忆表
CREATE TABLE memory (
                        id INT PRIMARY KEY AUTO_INCREMENT COMMENT '记忆记录ID',
                        user_id INT COMMENT '用户id',
                        word_id INT COMMENT '单词ID',
                        last_memory_time DATE COMMENT '上次记忆时间',
                        proficiency INT COMMENT '熟练度',
                        FOREIGN KEY(word_id) REFERENCES word(id),
                        FOREIGN KEY(user_id) REFERENCES user(id)
) COMMNENT ;


-- 创建用户签到记录表
CREATE TABLE user_sign_in (
                              id INT PRIMARY KEY AUTO_INCREMENT COMMENT '签到记录ID',
                              user_id INT COMMENT '用户id',
                              sign_in_year_month VARCHAR(16) COMMENT '签到年月',
                              record BIT(32) COMMENT '签到记录',
                              FOREIGN KEY (user_id) REFERENCES user(id), # 外键
                              UNIQUE INDEX idx_user_id_year_month (user_id, sign_in_year_month) # 唯一索引
);