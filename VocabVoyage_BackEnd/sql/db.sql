-- 创建数据库
CREATE DATABASE IF NOT EXISTS vocab_voyage;
USE vocab_voyage;

-- 创建用户表
CREATE TABLE user (
                      id INT AUTO_INCREMENT PRIMARY KEY COMMENT '用户ID',
                      nick_name VARCHAR(255) COMMENT '昵称',
                      phone VARCHAR(16) UNIQUE NOT NULL COMMENT '手机号',
                      password VARCHAR(64) COMMENT '用户密码',
                      coin INT DEFAULT 0 COMMENT '金币',
                      role VARCHAR(255) DEFAULT 'user' COMMENT '角色',
                      avatar VARCHAR(255) COMMENT '用户头像',
                      signature VARCHAR(255) COMMENT '用户签名'
) COMMENT '用户表';


-- 创建单词表
CREATE TABLE word (
                      id INT PRIMARY KEY AUTO_INCREMENT COMMENT '单词ID',
                      spell VARCHAR(255) NOT NULL COMMENT '拼写',
                      meaning VARCHAR(255) COMMENT '单词含义',
                      description VARCHAR(1024) COMMENT '单词描述'
) COMMENT '单词表';

-- 创建记忆表
CREATE TABLE memory (
                        id INT PRIMARY KEY AUTO_INCREMENT COMMENT '记忆记录ID',
                        user_id INT COMMENT '用户id',
                        word_id INT COMMENT '单词ID',
                        last_memory_time DATE COMMENT '上次记忆时间',
                        proficiency INT DEFAULT 0 COMMENT '熟练度: 0 ~ 100',
                        FOREIGN KEY(word_id) REFERENCES word(id),
                        FOREIGN KEY(user_id) REFERENCES user(id)
) COMMENT '单词记忆表';


-- 创建用户签到记录表
CREATE TABLE user_sign_in (
                              id INT PRIMARY KEY AUTO_INCREMENT COMMENT '签到记录ID',
                              user_id INT COMMENT '用户id',
                              sign_in_year_month VARCHAR(16) COMMENT '签到年月',
                              record BIT(32) COMMENT '签到记录',
                              FOREIGN KEY (user_id) REFERENCES user(id), # 外键
                              UNIQUE INDEX idx_user_id_year_month (user_id, sign_in_year_month) # 唯一索引
) COMMENT '签到记录表';


-- 创建单词错误表
CREATE TABLE mistake (
                         id INT PRIMARY KEY AUTO_INCREMENT COMMENT 'id',
                         word_id INT COMMENT '单词 id',
                         reporter_id  INT COMMENT '上报人 id',
                         solver_id INT COMMENT '解决人 id',
                         report_time DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL comment '上报时间',
                         resolved_time DATETIME DEFAULT NULL COMMENT '解决时间',
                         is_resolved TINYINT DEFAULT 0 COMMENT '是否解决',
                         description VARCHAR(512) COMMENT '错误描述',

                         FOREIGN KEY (reporter_id) REFERENCES user(id),
                         FOREIGN KEY (solver_id) REFERENCES user(id),
                         FOREIGN KEY (word_id) REFERENCES word(id)
) COMMENT '错误表';



# 视图：展示每个用户的单词记忆情况，包括记忆单词总数、熟练度分布等。
CREATE VIEW user_word_stats AS
SELECT u.id AS user_id, COUNT(m.id) AS total_memorized_words, AVG(m.proficiency) AS average_proficiency
FROM user u
         JOIN memory m ON u.id = m.user_id
GROUP BY u.id;