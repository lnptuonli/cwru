
Page({

  /**
   * 页面的初始数据
   */
  data: {
     file_name :'',
     info : [
       {
         name:'设备1',
         id: 'TEST1.csv'
       },
       {
         name: '设备2',
         id: 'TEST2.csv'
       },
       {
         name: '设备3',
         id: 'TEST3.csv'
       },
       {
         name: '设备4',
         id: 'TEST4.csv'
       },
       {
         name: '设备5',
         id: 'TEST5.csv'
       },
       {
         name: '设备6',
         id: 'TEST6.csv'
       },
       {
         name: '设备7',
         id: 'TEST7.csv'
       },
       {
         name: '设备8',
         id: 'TEST8.csv'
       },
       {
         name: '设备9',
         id: 'TEST9.csv'
       },
       {
         name: '设备10',
         id: 'TEST10.csv'
       },
       {
         name: '设备11',
         id: 'TEST11.csv'
       },
       {
         name: '设备12',
         id: 'TEST12.csv'
       },
       {
         name: '设备13',
         id: 'TEST13.csv'
       },
       {
         name: '设备14',
         id: 'TEST14.csv'
       },
       {
         name: '设备15',
         id: 'TEST15.csv'
       },
       {
         name: '设备16',
         id: 'TEST16.csv'
       },
       {
         name: '设备17',
         id: 'TEST17.csv'
       },
       {
         name: '设备18',
         id: 'TEST18.csv'
       },
       {
         name: '设备19',
         id: 'TEST19.csv'
       },
       {
         name: '设备20',
         id: 'TEST20.csv'
       },
     ]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    
  },
  zhoucheng1() {
    wx.navigateTo({
      url: '/pages/details/details?id=' + 1,
    })
  },
  zhoucheng2() {
    wx.navigateTo({
      url: '/pages/details/details?id=' + 2,
    })
  },
  zhoucheng3() {
    wx.navigateTo({
      url: '/pages/details/details?id=' + 3,
    })
  },
  zhoucheng4(){
    wx.navigateTo({
      url: '/pages/details/details?id='+ 4,
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
    
  },

})