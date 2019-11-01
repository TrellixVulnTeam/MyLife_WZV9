<template>
    <div>
        <div class="head-back">
            <div class="shard">
                <div class="title">
                    {{diary_item.name}}
                    <div class="title-inner">
                        {{diary_item.comment}} —— {{diary_item.date}}
                    </div>
                </div>
            </div>
        </div>
        <div class="content-area">
            <h2>{{diary_item.title}}</h2>
            <div class="content">
                {{diary_item.content}}
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'archives',
        data() {
            return {
                diary_item: "",
                localName: "diary_item"
            }
        },
        created() {
            if (localStorage.getItem(this.localName)) {
                this.diary_item = JSON.parse(localStorage.getItem(this.localName))
            } else {
                this.getDiaryInfo()
            }
        },
        mounted() {
            $('.head-back').css('background-image', 'url(' + this.diary_item.image + ')')
        },
        methods: {
            getDiaryInfo: function() {
                let me = this;
                let id = this.$route.params.id;

                this.$axios({
                    url: this.$host + '/api/diaryMsg/',
                    method: 'POST',
                    data: {'id': id}
                })
                .then(response => {
                    me.diary_item = response.data.content.item;
                    $('.head-back').css('background-image', 'url(' + me.diary_item.image + ')');
                    localStorage.setItem(this.localName, JSON.stringify(me.diary_item))
                })
            }
        },
        destroyed() {
            localStorage.removeItem(this.localName)
        },
    }
</script>

<style scoped>
.head-back {
    background-size: cover;
    background-repeat: no-repeat;
    background-position-y: -250px;
    transition: .3s;
}
.head-back .title {
    color: #403446;
}

.content-area {
    text-align: center;
}

.content-area h2 {
    padding-top: 50px;
    letter-spacing: 2px;
}
.content {
    text-align: center;
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
    padding: 20px;
    line-height: 26px;
    margin: 0 auto;
    width: 70%;
    border: 2px solid rgba(165, 146, 146, .3);
    border-radius: 10px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    background: rgba(236, 240, 241,1.0);
    margin: 20px auto;
    text-align: left;
}

@media (max-width: 1250px) {
    .content-area h2 {
        padding-top: 0;
    }
}

@media (max-width: 911px) {
    .head-back {
        background-position-y: -68px;
    }
    .content-area h2 {
        padding-top: 0;
        color: #778e8e;
    }
}
</style>
