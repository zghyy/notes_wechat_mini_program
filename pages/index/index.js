// pages/create/index.js
var serve = require('../../utils/myserveAPI')

Page({

    /**
     * 页面的初始数据
     */
    data: {
        items: [],
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
        let that = this;
        serve.getnote((data) => {
            var len = Object.keys(data).length
            var today = new Date()
            var thisYear = today.getFullYear()
            var thisMonth = (today.getMonth() + 1 < 10 ? '0' + (today.getMonth() + 1) : today.getMonth() + 1);
            var thisDay = (today.getDate() < 10 ? '0' + (today.getDate()) : today.getDate());

            for (let i = 0; i < len; i++) {
                var opdate = new Date(data[i]["updatetime"])
                data[i]["year"] = opdate.getFullYear();
                data[i]["month"] = (opdate.getMonth() + 1 < 10 ? '0' + (opdate.getMonth() + 1) : opdate.getMonth() + 1);
                data[i]["day"] = (opdate.getDate() < 10 ? '0' + (opdate.getDate()) : opdate.getDate());
                data[i]["countkey"]=i


                if(data[i]["year"]===thisYear && data[i]["month"]===thisMonth&&data[i]["day"]===thisDay){
                    data[i]["quality"] = "today"
                }
                else {
                    data[i]["quality"] = "none"
                }

            }
            console.log(data)
            this.setData({
                items: data
            })
        })

    },

    /**
     * 生命周期函数--监听页面初次渲染完成
     */
    onReady: function () {
    },

    /**
     * 生命周期函数--监听页面显示
     */
    onShow: function () {
        this.onLoad()
    },

    /**
     * 生命周期函数--监听页面隐藏
     */
    onHide: function () {

    },

    /**
     * 生命周期函数--监听页面卸载
     */
    onUnload: function () {

    },

    /**
     * 页面相关事件处理函数--监听用户下拉动作
     */
    onPullDownRefresh: function () {

    },

    /**
     * 页面上拉触底事件的处理函数
     */
    onReachBottom: function () {

    },

    /**
     * 用户点击右上角分享
     */
    onShareAppMessage: function () {

    },


    onNewItem: function (event) {
        wx.navigateTo({
            url: "/pages/create/index"
        })
    },
    onEditItem: function (event) {
        console.log(event.currentTarget.dataset.key)

        var json = this.data.items[event.currentTarget.dataset.key]
        console.log(json)
        wx.navigateTo({
            url: "/pages/edit/index?json="+JSON.stringify(json)
        })
    }
})