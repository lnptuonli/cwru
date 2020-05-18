Page({

  /**
   * 页面的初始数据
   */
  data: {
    listRotation:[
      { pic:'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588139674469&di=0b923204e36ba0d4bc188ae3b899b164&imgtype=0&src=http%3A%2F%2Fbbsfiles.vivo.com.cn%2Fvivobbs%2Fattachment%2Fforum%2F201710%2F16%2F152556yr5sdz4k294e9h7m.jpg'},
      { pic: 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588139649332&di=aaee0950f57f41c50ad9f7b979f1137e&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fblog%2F201512%2F07%2F20151207162033_Fsdei.jpeg' },
      { pic: 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1587554451161&di=d248fd1c668efbaf8be00aff321eff80&imgtype=0&src=http%3A%2F%2Fi-7.vcimg.com%2Ftrim%2Ff88337a540e7fd6b83c3bdce090d6801354171%2Ftrim.jpg' }
    ],
    autoplay:true,
    indicatorDots: true
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    
  },
  jiance(){
    wx.switchTab({
      url: '/pages/weixiu/weixiu',
    })
  },
  yunwei(){
    wx.switchTab({
      url: '/pages/yunwei/yunwei',
    })
  },
  yujing(){
    wx.switchTab({
      url: '/pages/yunwei/yunwei',
    })
  },
  lishi(){
    wx.switchTab({
      url: '/pages/weixiu/weixiu',
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
    
  }
})