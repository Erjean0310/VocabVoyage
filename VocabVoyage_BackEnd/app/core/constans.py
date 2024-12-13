class Constants:

    DB_ERROR = "数据库处理异常!"
    USER_HAS_SIGNED_IN = "您已经签到!"
    USER_NOT_LOG_IN = "当前未登录, 请先登录!"
    SESSION_EXPIRE = "会话已过期, 请重新登录!"
    SESSION_INVALID = "当前会话状态异常!"
    VERIFICATION_FAILED = "账号或密码错误!"
    LOGIN_SUCCESS = "登录成功!"
    PHONE_ALREADY_REGISTERED = "该电话号码已经存在!"
    REGISTER_SUCCESS = "注册成功!"
    LOGOUT_SUCCESSFUL = "登出成功!"
    SIGN_IN_SUCCESS = "签到成功!"
    MODIFY_PASSWORD_SUCCESS = "密码修改成功"

    ADMIN_ROLE = 'admin'
    PERMISSION_ERROR = "权限不足"

    # 单词记忆常量
    FAMILIAR_WORD_WEIGHT = 0.1
    DEFAULT_MEMORIZE_WORD_COUNT = 10

    WORD_NOT_FOUND = "找不到该单词信息"

    REPORT_SUCCESS = "上报成功"

    # 大模型相关常量
    OPENAI_PROMPT = "你是一名英语老师"
    DEFAULT_MODEL = "gpt-4o-mini"
    DEFAULT_STREAM_ENABLED = True


    DEFAULT_AVATAR_URL = "http://vocab-voyage.oss-cn-beijing.aliyuncs.com/default_avatar.png"

