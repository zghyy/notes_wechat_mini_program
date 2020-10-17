// pages/create/index.js
var serve = require('../../utils/myserveAPI')

Page({

    /**
     * 页面的初始数据
     */
    data: {
        item: {
            "title": "",
            "content": "",
        }
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {

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

    onSubmit: function (event) {
        var item = this.data.item;
        item.title = event.detail.value.title;
        item.content = event.detail.value.content;
        this.setData({
            item: item
        });
        console.log(this.data.item)
        serve.addnote((data) => {
            if (data === "done") {
                wx.showToast({
                    title: "保存成功",
                    success: function () {
                        // 返回首页
                        setTimeout(function () {
                            wx.hideToast();
                            wx.navigateBack();
                        }, 1000)
                    }
                })
            }
        }, this.data.item)
    }
})