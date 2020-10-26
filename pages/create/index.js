// pages/create/index.js
var serve = require('../../utils/myserveAPI')

Page({

    data: {
        item: {
            "title": "",
            "content": "",
        }
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