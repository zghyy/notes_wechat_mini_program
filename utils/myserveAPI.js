var GETNOTE = "https://api.zghy.xyz/getnote"
// var ADDNOTE = "http://zghy.xyz:23333/addnote"
// var DELNOTE = "http://zghy.xyz:23333/delnote"
// var EDITNOTE = "http://zghy.xyz:23333/editnote"

function getnote(callback) {
    wx.request({
        url:GETNOTE,
        data:{},
        method:'GET',
        success:function (res) {
            console.log(1)
            console.log(res.data)
            callback(res.data)
            return res.data
        }
    })
}

module.exports = {
    getnote:getnote,
}