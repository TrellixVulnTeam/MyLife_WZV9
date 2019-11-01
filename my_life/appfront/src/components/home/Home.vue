<template>
  <div id="HomeInfo">
    <div class="head-back">
        <div class="shard">
            <div class="title">
                与命运不公平的抗战...
                <div class="title-inner">
                    如果是你,一定可以做到...
                </div>
            </div>
        </div>
    </div>
    <div class="MainInfo">
        <div class="container">
            <div class="box" v-for="diary in diary_list">
                <div class="imgBx" >
                    <img :src="diary.image" alt="">
                </div>
                <div class="content" @click="diaryAbout(diary.id)">
                    <div class="date">
                        <h6>{{ diary.name }}・{{ diary.date }}・{{ diary.classification }}</h6>
                    </div>
                    <div>
                        <h2>{{ diary.title }}</h2>
                        <p>{{ diary.comment }}</p>
                    </div>
                </div>
            </div>
            <div class="prev-center">
                <a href="#" title="上一页"><span></span><span></span>Prev Here</a>
            </div>
            <div class="next-center">
                <a href="#" title="下一页"><span></span><span></span>Next Here</a>
            </div>
        </div>
    </div>
    <div id="footer">
    <p>
        —— 啊，<span class="inner">奎尔萨拉斯森林</span>
        还是那么的美丽，记得当我还是个小孩子的时候曾来过这里。现在我们将踏平这里！
        </p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      diary_list: null
    }
  },
  mounted() {
    this.getDiaryLift()
  },
  methods: {
    getDiaryLift: function() {
      let me = this;
      this.$axios({
        url: this.$host + '/api/diaryInfo',
        method: 'GET'
      })
      .then(response => {
        me.diary_list = response.data.content.list;
      })
    },
    diaryAbout: function(id) {
        let params = {id: id}
        this.$router.push({name: 'archives', params: params})
    },
  }
}

</script>

<style scoped>
#HomeInfo {
  position: relative;
}

.MainInfo {
    display: flex;
    justify-content: center;
    align-items: center;
}

.container {
    position: relative;
    width: 1100px;
    display: flex;
    flex-wrap: wrap;
}

.container .box {
    position: relative;
    width: 78%;
    height: 250px;
    overflow: hidden;
    transition: .5s;
    cursor: pointer;
    margin: 50px auto;
    box-shadow: 0 5px 10px rgba(0, 0, 0, .1);
}

.container .box .content .date {
    position: absolute;
    top: -40px;
    color: #fff;
    transition: .5s;
    text-transform: uppercase;
    margin-bottom: 5px;
    font-size: 20px;
}

.container .box .content .date h6 {
    font-size: 16px;
    font-weight: 300;
}

.container .box:hover {
    z-index: 1;
    transform: scale(1.1);
    box-shadow: 0 25px 40px rgba(0, 0, 0, .5);
    border-radius: 10px;
}

.container .box .imgBx {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border-radius: 10px;
}

.container .box .imgBx:before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1;
    /*background: linear-gradient(180deg, #f00, #000);*/
    mix-blend-mode: multiply;
    opacity: 0;
    transition: .5s;
    border-radius: 10px;
}

.container .box:hover .imgBx:before {
    opacity: 1;
}

.container .box .imgBx img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 10px;
}

.container .box .content {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1;
    display: flex;
    align-items: flex-end;
    border-radius: 10px;
}

.container .box .content div {
    padding: 20px;
}

.container .box .content h2 {
    color: #fff;
    transition: .5s;
    text-transform: uppercase;
    margin-bottom: 5px;
    font-size: 20px;
    transform: translateY(200px);
}

.container .box:hover .content h2 {
    transform: translateY(0);
    transition-delay: .6s;
}

.container .box .content p {
    color: #fff;
    transform: translateY(200px);
    transition: .5s;
    font-size: 14px;
}

.container .box:hover .content p {
    transform: translateY(0);
    transition-delay: .7s;
}

/*------------------------------------------------------------------*/
/*下一页按钮*/
.next-center {
    position: absolute;
    right: -95px;
    bottom: 40px;
}

.next-center a {
    display: inherit;
    width: 150px;
    height: 50px;
    color: #262626;
    font-size: 20px;
    background: rgba(255, 255, 255, .2);
    text-align: center;
    line-height: 50px;
    text-transform: uppercase;
    border: 2px solid #262626;
    transition: .5s;
    transform: skew(15deg);
}

.next-center a:hover {
    background: rgba(79, 156, 255, .9);
    color: #fff;
}

.next-center span:nth-child(1) {
    position: absolute;
    width: 15px;
    height: 100%;
    border: 2px solid #262626;
    background: #efefef;
    top: 6px;
    left: -19px;
    transform: skewY(-45deg);
}

.next-center span:nth-child(2) {
    position: absolute;
    width: 100%;
    height: 15px;
    border: 2px solid #262626;
    background: #efefef;
    bottom: -19px;
    right: 6px;
    transform: skewX(-45deg);
    box-shadow: 0 40px 25px rgba(0, 0, 0 .2);
}

/*------------------------------------------------------------------*/
/*prev*/
.prev-center {
    position: absolute;
    left: -95px;
    bottom: 40px;
}

.prev-center a {
    display: inherit;
    width: 150px;
    height: 50px;
    color: #262626;
    font-size: 20px;
    background: rgba(255, 255, 255, .2);
    text-align: center;
    line-height: 50px;
    text-transform: uppercase;
    border: 2px solid #262626;
    transition: .5s;
    transform: skew(-15deg);
}

.prev-center a:hover {
    background: rgba(79, 156, 255, .9);
    color: #fff;
}

.prev-center span:nth-child(1) {
    position: absolute;
    width: 15px;
    height: 100%;
    border: 2px solid #262626;
    background: #efefef;
    top: 8px;
    right: -19px;
    transform: skewY(45deg);
}

.prev-center span:nth-child(2) {
    position: absolute;
    width: 100%;
    height: 15px;
    border: 2px solid #262626;
    background: #efefef;
    bottom: -19px;
    right: -10px;
    transform: skewX(45deg);
    box-shadow: 0 40px 25px rgba(0, 0, 0 .2);
}

/*------------------------------------------------------------------*/
/*页脚*/
#footer {
    width: 100%;
    height: 30px;
    text-align: center;
}

#footer p {
    text-align: center;
    font-size: 12px;
    letter-spacing: 1px;
    color: #9e8181;
    display: inline-block;
}

#footer span.inner {
    color: red;
}

/*------------------------------------------------------------------*/
@media (max-width: 1300px) {
    .next-center {
        bottom: -30px;
        right: 30px;
        margin-bottom: 30px;
    }

    .next-center a {
        width: 100px;
        height: 30px;
        line-height: 30px;
        font-size: 12px;
    }

    .prev-center {
        bottom: -30px;
        left: 30px;
        margin-bottom: 30px;
    }

    .prev-center a {
        width: 100px;
        height: 30px;
        line-height: 30px;
        font-size: 12px;
    }
}

@media (max-width: 991px) {
    .container .box {
        margin: 25px auto;
        width: 85%;
        height: 200px;
    }

    .container .box .content .date h6 {
        font-size: 12px;
        font-weight: 300;
    }

    .next-center {
        bottom: -70px;
        right: 30px;
        margin-bottom: 30px;
    }

    .next-center a {
        width: 100px;
        height: 30px;
        line-height: 30px;
        font-size: 12px;
    }

    .next-center span:nth-child(1) {
        width: 7px;
        height: 100%;
        top: 2px;
        left: -11px;
    }

    .next-center span:nth-child(2) {
        width: 100%;
        height: 7px;
        bottom: -11px;
        right: 2px;
    }

    .prev-center {
        bottom: -70px;
        left: 30px;
        margin-bottom: 30px;
    }

    .prev-center a {
        width: 100px;
        height: 30px;
        line-height: 30px;
        font-size: 12px;
    }

    .prev-center span:nth-child(1) {
        width: 7px;
        height: 100%;
        top: 4px;
        right: -11px;
    }

    .prev-center span:nth-child(2) {
        width: 100%;
        height: 7px;
        bottom: -11px;
        right: -6px;
    }

    #footer {
        position: relative;
        bottom: -60px;
    }

    #footer p {
        padding: 0 40px;
        font-size: 10px;
    }
}

@media (max-width: 500px) {
    .container .box:first-child {
        margin-top: 0;
    }
}
</style>
