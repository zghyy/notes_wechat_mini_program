var GETNOTE = "http://zghy.xyz:23333/getnote"
var ADDNOTE = "http://zghy.xyz:23333/addnote"
var DELNOTE = "http://zghy.xyz:23333/delnote"
var EDITNOTE = "http://zghy.xyz:23333/editnote"

function getnote() {
    wx.request({
        url:GETNOTE,
        data:{},
        method:'GET',
        success:function (res) {
            return res.data
        }
    })
}

module.exports = {
    getnote:getnote,
}