var app = new Vue({
    el: '.MainInfo',
    data: {
        diary_list: null
    },
    mounted() {
        this.getDiaryList();
    },
    methods: {
        getDiaryList: function () {
            var me = this;
            axios({
                url: '/api/diaryInfo',
                method: 'GET',
            })
                .then((response) => {
                    me.diary_list = response.data.content.list;
                });
        },
        getInfo: function (id) {
            axios({
                url: '/archives',
                method: 'GET',
                params: {
                    'life-share': id
                }
            })
                .then(response => $('.MainInfo').html(response.data))
        },
    }
});


