<template>
  <div id="app">
    <div id="nav">
        <header>
            <div class="logo">ARCHER'♇</div>
            <nav>
                <ul>
                    <li><a @click="pushRouter(sites[0].Home)">Home <i class="fas fa-home"></i></a></li>
                    <li><a @click="pushRouter(sites[0].Home)">About <i class="fas fa-address-card"></i></a></li>
                    <li><a @click="pushRouter(sites[0].Home)">Services</a></li>
                    <li><a @click="pushRouter(sites[0].Home)">Team</a></li>
                    <li><a @click="pushRouter(sites[0].Home)">Portfolio</a></li>
                    <li><a class="music-bar">Music <i class="fas fa-music"></i></a></li>
                </ul>
            </nav>
            <div class="menu-toggle"><i class="fa fa-bars" aria-hidden="true"></i></div>
        </header>
        <div class="aplayer" data-id="7231371581" data-server="tencent" data-type="playlist" data-mode="circulation" data-preload="auto" storage-name="metingjs" theme="#2980b9" autoplay="false" list-max-height="300px" order="random" mutex="true" audio.theme></div>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
      return {
          sites: [  // 存放导航栏url去往的路由name
              {'Home': 'Home'}
          ]
      }
  },
  methods: {
      pushRouter: function(name) {
          if (this.$route.name !== name) {
              this.$router.push({name: name})
          }
      },
  },
}

$(document).ready(function () {
  $('.menu-toggle').click(function () {
    $('nav').toggleClass('active')
  })
  $('.logo').on('click', function () {
    let aplayer = $('.aplayer');
    if (aplayer.hasClass('show')) {
        aplayer.removeClass('show');
    }
  });
  $('nav').bind({
    // 'touchstart mousedown' : function(){},
    // 'touchmove mousemove' : function(){},
    'touchend touchcancel mouseup': function () {
        $(this).removeClass('active');
    }
  });
  $('.music-bar').click(function () {
    $('.aplayer').toggleClass('show')
  });

  var date_time = new Date();

  if (date_time.getHours() >= 15)
    $('body').css('background', 'rgba(253, 205, 205, 0.8)');
  if (date_time.getHours() >= 18)
    $('body').css('background', 'rgba(44, 42, 42, 1)');
});
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  height: 100vh;
  width: 100%;
}

#appInfo {
  position: relative;
  background: #fbfbfb;
  width: 100%;
}

ul {
    margin: 0;
    padding: 0;
}

li {
    list-style: none;
}

a {
    text-decoration: none;
}

/*滚动条宽高*/
body::-webkit-scrollbar {
    width: 5px;
    height: 8px;
}

/*正常情况下滑块的样式*/
body::-webkit-scrollbar-thumb {
    background-color: rgba(0, 0, 0, .6);
    border-radius: 10px;
}

/*鼠标悬浮在该类指向的控件上时滑块的样式*/
body:hover::-webkit-scrollbar-thumb {
    background-color: rgba(0, 0, 0, .7);
    border-radius: 10px;
    box-shadow: inset 1px 1px 0 rgba(0, 0, 0, .1);
}

/*鼠标悬浮在滑块上时滑块的样式*/
body::-webkit-scrollbar-thumb:hover {
    background-color: rgba(0, 0, 0, .3);
    box-shadow: inset 1px 1px 0 rgba(0, 0, 0, .1);
}

/*正常时候的主干部分*/
body::-webkit-scrollbar-track {
    border-radius: 10px;
    box-shadow: inset 0 0 6px rgba(0, 0, 0, 0);
    background-color: rgba(0, 0, 0, .7);
}

/*鼠标悬浮在滚动条上的主干部分*/
body::-webkit-scrollbar-track:hover {
    box-shadow: inset 0 0 6px rgba(0, 0, 0, .4);
    background-color: rgba(0, 0, 0, .01);
}
body {
  background: #fbfbfb;
}
#nav .aplayer {
    position: fixed;
    z-index: 999;
    bottom: -310px;
    width: 50%;
    left: 50%;
    transform: translate(-50%, 0);
    border-radius: 15px;
    box-shadow: 1px 5px 10px rgba(0, 0, 0, .2);
    transition: 0.5s;
}
#nav .aplayer.show {
    bottom: 0;
}
header {
    position: fixed;
    z-index: 2;
    top: 0;
    left: 0;
    padding: 0 100px;
    background: rgba(0, 0, 0, .5);
    width: 100%;
    box-sizing: border-box;
}
header .logo {
    color: #fff;
    height: 50px;
    line-height: 50px;
    font-size: 24px;
    float: left;
    font-weight: bold;
}
header nav {
    float: right;
}
header nav.active {
    left: 0;
}
header nav ul {
    display: flex;
}
header nav ul li a {
    height: 50px;
    line-height: 50px;
    padding: 0 20px;
    color: #fff;
    display: block;
    transition: 0.2s;
    cursor: pointer;
    font-size: 13px;
}
header nav ul li a:hover {
    color: #fff;
    background: #2196f3;
}
.menu-toggle {
    color: #fff;
    float: right;
    line-height: 50px;
    font-size: 24px;
    padding-top: 10px;
    cursor: pointer;
    display: none;
}
#nav .aplayer {
    position: fixed;
    z-index: 999;
    max-height: 300px;
    bottom: -310px;
    width: 50%;
    left: 50%;
    transform: translate(-50%, 0);
    border-radius: 15px;
    box-shadow: 1px 5px 10px rgba(0, 0, 0, .2);
    transition: 0.5s;
}
#nav .aplayer.show {
    bottom: 0;
}
header {
    position: fixed;
    z-index: 2;
    top: 0;
    left: 0;
    padding: 0 100px;
    background: rgba(0, 0, 0, .5);
    width: 100%;
    box-sizing: border-box;
}
header .logo {
    color: #fff;
    height: 50px;
    line-height: 50px;
    font-size: 24px;
    float: left;
    font-weight: bold;
}
header nav {
    float: right;
}
header nav.active {
    left: 0;
}
header nav ul {
    display: flex;
}
header nav ul li a {
    height: 50px;
    line-height: 50px;
    padding: 0 20px;
    color: #fff;
    display: block;
    transition: 0.2s;
    cursor: pointer;
    font-size: 13px;
}
header nav ul li a:hover {
    color: #fff;
    background: #2196f3;
}
.menu-toggle {
    color: #fff;
    float: right;
    line-height: 50px;
    font-size: 24px;
    padding-top: 10px;
    cursor: pointer;
    display: none;
}
.head-back {
    position: relative;
    height: 400px;
    background: url("../static/images/head_icon.jpg");
    background-size: cover;
    background-position-y: -70px;
    background-repeat: no-repeat;
    transition: .3s;
}
.head-back .shard {
    position: absolute;
    left: 50%;
    top: 40%;
    transform: translate(-50%, -40%);
}
.head-back div {
    cursor: pointer;
    margin: 10px auto;
}
.head-back .title {
    text-align: center;
    font-size: 40px;
    font-weight: 300;
    color: #fff;
}
.head-back .title .title-inner {
    font-size: 16px;
    font-weight: 400;
    text-align: center;
}

/* ---- 响应 */
@media (max-width: 991px) {
    header {
        padding: 0 20px;
    }

    .menu-toggle {
        display: block;
        padding-top: 0;
    }

    header nav {
        position: absolute;
        width: 100%;
        height: calc(100vh - 50px);
        background: #333;
        top: 50px;
        left: -100%;
        transition: 0.5s;
    }

    header nav.active {
        left: 0;
    }

    header nav ul {
        display: block;
        text-align: center;
    }

    header nav ul li a {
        border-bottom: 1px solid rgba(0, 0, 0, .2);
    }

    .head-back .title {
        font-size: 24px;
        transition: .5s;
    }

    #nav .aplayer {
        width: 90%;
    }
}

@media (max-width: 375px) {
    .head-back .title {
        font-size: 16px;
    }

    .head-back .title .title-inner {
        font-size: 12px;
    }

    .aplayer {
        width: 100%;
    }
}
/*  */
</style>
