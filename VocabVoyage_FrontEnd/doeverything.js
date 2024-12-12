
document.addEventListener('DOMContentLoaded', function () {
    /* 发音 */
    const playPauseBtns = document.getElementsByClassName('playPauseBtn fas fa-play-circle');
    const audios = document.getElementsByClassName('audio');
    for (let i = 0; i < playPauseBtns.length; i++) {
        const playPauseBtn = playPauseBtns[i];
        const audio = audios[i];
        /* 点击按钮时播放发音 */
        playPauseBtn.addEventListener('mousedown', function (event) {
            event.stopPropagation();
            if (audio.paused) {
                audio.play();/* 播放对应的音频 */
                playPauseBtn.classList.remove('fa-play-circle');
                playPauseBtn.classList.add('fa-pause-circle'); // 切换为暂停图标
            } else {
                audio.pause();/* 暂停对应的音频 */
                playPauseBtn.classList.remove('fa-pause-circle');
                playPauseBtn.classList.add('fa-play-circle'); // 切换为播放图标
            }
        });
        /* 发音播放完毕后，切换成播放图标 */
        audio.addEventListener('ended', function () {
            playPauseBtn.classList.remove('fa-pause-circle');
            playPauseBtn.classList.add('fa-play-circle');
        });
    }


    /* 进度条 */
    const getPassBtns = document.getElementsByClassName('get');
    const bar = document.getElementById("bar");
    for (let i = 0; i < getPassBtns.length; i++) {
        const getPassBtn = getPassBtns[i];
        getPassBtn.addEventListener('mousedown', function (event) {
            event.stopPropagation();
            const widths = ['10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%'];
            bar.style.width = widths[i];
        });
    }


    /* 用户盒子 */
    const usericon = document.getElementById('usericon');
    const userbox = document.getElementById('userbox');
    /* 点击用户图标时，显示用户盒子 */
    usericon.addEventListener('click', function (event) {
        event.stopPropagation();
        userbox.style.animation = 'slideIn 1s forwards';
        userbox.style.display = 'block';
    });
    // 点击其他地方时，隐藏用户盒子
    document.addEventListener('click', function (event) {
        if (!usericon.contains(event.target) && !userbox.contains(event.target)) {
            userbox.style.animation = 'slideOut 2s forwards';
        }
    });
    // 防止点击目标元素时隐藏用户盒子
    userbox.addEventListener('click', function (event) {
        /* 阻止事件冒泡 */
        event.stopPropagation();
    });


    /* 日历盒子的弹出与隐藏 */
    const calendaricon = document.getElementById('calendaricon');
    const calendarbox = document.getElementById('calendarbox');
    /* 点击日历图标时，显示日历盒子 */
    calendaricon.addEventListener('click', function (event) {
        event.stopPropagation();
        calendarbox.style.animation = 'slideIn 1s forwards';
        calendarbox.style.display = 'block';
    });
    // 点击其他地方时，隐藏日历盒子
    document.addEventListener('click', function (event) {
        if (!calendaricon.contains(event.target) && !calendarbox.contains(event.target)) {
            calendarbox.style.animation = 'slideOut 2s forwards';
        }
    });
    // 防止点击目标元素时隐藏日历盒子
    calendarbox.addEventListener('click', function (event) {
        /* 阻止事件冒泡 */
        event.stopPropagation();
    });


    /* 单词盒子 */
    const wordboxs = document.getElementsByClassName('wordbox');
    const worddetailbox = document.getElementById('worddetail');
    for (let i = 0; i < wordboxs.length; i++) {
        const wordbox = wordboxs[i];
        /* 点击单词盒子时变长 */
        /* wordbox.addEventListener('mousedown', function (event) {
            wordbox.style.animation = 'biggerwordbox 1s forwards';
            document.addEventListener('mouseup', function (event) {
                wordbox.style.animation = 'smallerwordbox 1s forwards';
            });
        }); */
        /* 点击单词盒子时在屏幕中间展示详细信息盒子 */
        wordbox.addEventListener('click', function (event) {
            event.stopPropagation();
            userbox.style.animation = 'slideOut 2s forwards';
            calendarbox.style.animation = 'slideOut 2s forwards';
            worddetailbox.style.animation = 'slideIn 1s forwards';
            worddetailbox.style.display = 'block';
        })
        /* 点击其他地方时隐藏详细信息盒子 */
        document.addEventListener('click', function (event) {
            if (!wordbox.contains(event.target)) {
                worddetailbox.style.animation = 'slideOut 2s forwards';
            }
        })
        worddetailbox.addEventListener('click', function (event) {
            event.stopPropagation();
        })
    }
});

