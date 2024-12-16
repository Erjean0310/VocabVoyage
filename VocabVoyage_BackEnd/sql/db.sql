-- 创建用户 vv_user
CREATE USER 'vv_user'@'%' IDENTIFIED BY '412412';

-- 授予权限
GRANT SELECT, INSERT, UPDATE, DELETE ON vocab_voyage.* TO 'vv_user'@'%';

-- 应用权限更改
FLUSH PRIVILEGES;






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



-- 视图
SELECT
    `u`.`id` AS `user_id`,
    count( `m`.`id` ) AS `total_memorized_words`,
    avg( `m`.`proficiency` ) AS `average_proficiency`
FROM
    ( `user` `u` JOIN `memory` `m` ON ( ( `u`.`id` = `m`.`user_id` ) ) )
GROUP BY
    `u`.`id`;


-- 存储过程
CREATE DEFINER=`root`@`%` PROCEDURE `update_proficiency`(IN p_word_id INT, IN p_user_id INT, IN mem_res INT)
BEGIN
    DECLARE current_proficiency INT DEFAULT 0;
    -- 尝试获取当前熟练度，如果不存在则设置为默认值
    SELECT proficiency INTO current_proficiency
    FROM memory
    WHERE user_id = p_user_id AND word_id = p_word_id;
    -- 根据记忆结果更新熟练度
    CASE mem_res
        WHEN 1 THEN
            SET current_proficiency = FLOOR(current_proficiency * 0.7 + 100 * 0.3);
        WHEN 2 THEN
            SET current_proficiency = FLOOR(current_proficiency * 0.9);
        WHEN 3 THEN
            SET current_proficiency = FLOOR(current_proficiency * 0.3);
        ELSE
            -- 如果 mem_res 不是 1、2 或 3，可以设置为默认值或抛出错误
            SET current_proficiency = 0; -- 或者可以选择抛出错误
        END CASE;
    -- 如果用户和单词都存在，更新熟练度和最后记忆时间；否则插入新记录，熟练度设为 6
    IF EXISTS (SELECT 1 FROM memory WHERE user_id = p_user_id AND word_id = p_word_id) THEN
        UPDATE memory
        SET proficiency = current_proficiency, last_memory_time = CURDATE()
        WHERE user_id = p_user_id AND word_id = p_word_id;
    ELSE
        INSERT INTO memory (user_id, word_id, last_memory_time, proficiency)
        VALUES (p_user_id, p_word_id, CURDATE(), current_proficiency);
    END IF;
END;

-- 触发器1
create definer = root@`%` trigger sign_id_addcoin
    after update
                     on user_sign_in
                     for each row
BEGIN
    IF NEW.record <>OLD.record
THEN
UPDATE user
SET coin = coin + 1
WHERE user.id = NEW.user_id;
END IF;
END;


-- 触发器2
create definer = root@`%` trigger sign_id_addcoin2
    after insert
    on user_sign_in
    for each row
BEGIN
    Update user
    set coin = coin + 1
    where user.id = New.user_id;
END;

