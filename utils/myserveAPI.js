var GETNOTE = "https://api.zghy.xyz/getnote"
var ADDNOTE = "https://api.zghy.xyz/addnote"
var DELNOTE = "https://api.zghy.xyz/delnote"
var EDITNOTE = "https://api.zghy.xyz/editnote"


function getnote(callback) {
    wx.request({
        url:GETNOTE,
        data:{},
        method:'GET',

        success:function (res) {
            callback(res.data)
        }
    })
}

function addnote(callback,notedata){
    console.log(notedata)
    wx.request({
        url:ADDNOTE,
        data:notedata,
        method:'POST',
        header: {
            "Content-Type": "application/x-www-form-urlencoded" //用于post
        },
        success:function (res) {
            callback(res.data)
        }
    })
}




module.exports = {
    getnote:getnote,
    addnote:addnote
}