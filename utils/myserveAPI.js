var GETNOTE = "https://api.zghy.xyz/getnote"
var ADDNOTE = "https://api.zghy.xyz/addnote"
var DELNOTE = "https://api.zghy.xyz/delnote"
var EDITNOTE = "https://api.zghy.xyz/editnote"


function getnote(callback) {
    wx.request({
        url: GETNOTE,
        data: {},
        method: 'GET',

        success: function (res) {
            callback(res.data)
        }
    })
}

function addnote(callback, notedata) {
    wx.request({
        url: ADDNOTE,
        data: notedata,
        method: 'POST',
        header: {
            "Content-Type": "application/x-www-form-urlencoded" //用于post
        },
        success: function (res) {
            callback(res.data)
        }
    })
}

function editnote(callback, notedata) {
    var json = {
        "notekey": notedata["notekey"],
        "title": notedata["title"],
        "content": notedata["content"]
    }
    console.log(json)
    wx.request({
        url: EDITNOTE,
        data: json,
        method: 'POST',
        header: {
            "Content-Type": "application/x-www-form-urlencoded" //用于post
        },
        success: function (res) {
            console.log(res.data)
            callback(res.data)
        }
    })
}

function delnote(callback, notedata) {
    var json = {"notekey": notedata}
    wx.request({
        url: DELNOTE,
        data: json,
        method: 'POST',
        header: {
            "Content-Type": "application/x-www-form-urlencoded" //用于post
        },
        success: function (res) {
            callback(res.data)
        }
    })
}


module.exports = {
    getnote: getnote,
    addnote: addnote,
    delnote: delnote,
    editnote: editnote
}