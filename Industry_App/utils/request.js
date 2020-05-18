var app = getApp
var host = 'https://api.phmlearn.com/'
/**
 * url 接口
 * postData json参数
 * doSucess  成功回调
 * doFail 失败回调
 */

function postRequest(url, data) {
  return new Promise((resolve, reject) => {
    wx.showLoading({
      title: '加载中',
    })
    wx.request({
      url:`${host}${url}`,
      header: {
        "content-type": "application/x-www-form-urlencoded"
      },
      method: 'POST',
      data,
      success: res => {
        wx.hideLoading()
        resolve(res)
      },
      fail: err => {
        reject(err)
      }
    })
  })
}

function getRequest(url, data) {
  return new Promise((resolve, reject) => {
    wx.showLoading({
      title: '加载中',
    })
    wx.request({
      url: `${host}${url}`,
      method: 'get',
      data,
      success: res => {
        wx.hideLoading()
        resolve(res)
      },
      fail: err => {
        reject(err)
      }
    })
  })
}


module.exports.getRequest = getRequest;
module.exports.postRequest = postRequest;
