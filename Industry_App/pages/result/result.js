const Http = require('../../utils/request.js');
const app = getApp();
import * as echarts from '../../ec-canvas/echarts';
var Chart = null;
Page({

  /**
   * 页面的初始数据
   */
  data: {
    num:1,
    ec: {
      onInit: function (canvas, width, height) {
        chart = echarts.init(canvas, null, {
          width: width,
          height: height
        });
        canvas.setChart(chart);
        return chart;
      },
      lazyLoad: true // 延迟加载
    },
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
  
  },
  //初始化图表
  init_echarts: function () {
    this.echartsComponnet.init((canvas, width, height) => {
      // 初始化图表
      const Chart = echarts.init(canvas, null, {
        width: width,
        height: height
      });
      this.setOption(Chart)
      // 注意这里一定要返回 chart 实例，否则会影响事件处理等
      return Chart;
    });
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
  
    var json = {
      "username": "1003721463",
      "password": "youarea2b"
    }
    Http.postRequest("auth/apiInfo", json).then(res => {
      if (res.data.success) {
        var json = {
          "api_key": res.data.data.apiKey,
          "api_secret": res.data.data.apiSecret
        }
        Http.postRequest("auth/access_token", json).then(res => {
          if (res.data.success) {
            var json = {
              "access_token": res.data.data.access_token,
              "file_name": "TEST3.csv"
            }
            Http.postRequest("component/upload/2/88", json).then(res => {
              if (res.data.success) {
                this.setData({
                  file_name: res.data.data.file_name
                })
                var json = {
                  "username": "13671075682",
                  "password": "990220qaz"
                }
                Http.postRequest("auth/apiInfo", json).then(res => {
                  var json = {
                    "api_key": res.data.data.apiKey,
                    "api_secret": res.data.data.apiSecret
                  }
                  Http.postRequest("auth/access_token", json).then(res => {

                    var json = {
                      "access_token": res.data.data.access_token,
                      "file_name": this.data.file_name
                    }
                    Http.postRequest("component/upload/ML/model/59/124", json).then(res => {
                     
                     console.log(res)
                      var predict = res.data.data.predict
                      this.echartsComponnet = this.selectComponent('#mychart');
                      //如果是第一次绘制
                      if (!Chart) {
                        this.init_echarts(); //初始化图表
                      } else {
                        this.setOption(Chart); //更新数据
                      }
                     var list = new Array
                      for (let i = 0; i < predict.length;i++){
                        var value = predict[i]
                        list.push(value)
                        Math.max(...list)
                        //判断数字出现的概率
                        this.refrain(list)
                      }
                      
                      var success = res.data.data.success
                        this.setData({
                        predict
                      })
                    })
                  })

                })

              }
            })

          }
        })
      }
    })
  },
   refrain(arr) {
    　　var tmp = [];
    　　if(Array.isArray(arr)) {
  　　　　arr.concat().sort().sort(function (a, b) {
    　　　　　　if (a == b && tmp.indexOf(a) === -1) tmp.push(a);
  　　　　});
        var state = ''
        var status = ''
        if (tmp == 0){
          state = '正常'
          status = '100%'
        } else if (tmp == 1){
          state = '滚动体故障'
          status = '100%'
        } else if (tmp == 2) {
          state = '外圈故障'
          status = '100%'
        }else{
          state = '内圈故障'
          status = '100%'
        }
        this.setData({
          state,
          status
        })
        
　　}
　　return tmp;
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
  res(e) {
    var num = 1
    var n = wx.getStorageSync('number')
    var number = num + n
    if (number>142){
      number = 1
    }else{
      number = num + n
    }
    wx.setStorage({
      key: 'number',
      data: number,
    })
    console.log(wx.getStorageSync('number'),"num")
    var json = {
      "username": "1003721463",
      "password": "youarea2b"
    }
    Http.postRequest("auth/apiInfo", json).then(res => {
      if (res.data.success) {
        var json = {
          "api_key": res.data.data.apiKey,
          "api_secret": res.data.data.apiSecret
        }
        Http.postRequest("auth/access_token", json).then(res => {
          if (res.data.success) {
            var json = {
              "access_token": res.data.data.access_token,
              "file_name": "TEST" + wx.getStorageSync('number')+".csv"
            }
            Http.postRequest("component/upload/2/88", json).then(res => {
              if (res.data.success) {
                this.setData({
                  file_name: res.data.data.file_name
                })
                var json = {
                  "username": "13671075682",
                  "password": "990220qaz"
                }
                Http.postRequest("auth/apiInfo", json).then(res => {
                  var json = {
                    "api_key": res.data.data.apiKey,
                    "api_secret": res.data.data.apiSecret
                  }
                  Http.postRequest("auth/access_token", json).then(res => {

                    var json = {
                      "access_token": res.data.data.access_token,
                      "file_name": this.data.file_name
                    }
                
                   
                    Http.postRequest("component/upload/ML/model/59/124", json).then(res => {
                     
                      var predict = res.data.data.predict
                      this.echartsComponnet = this.selectComponent('#mychart');
                      //如果是第一次绘制
                      if (!Chart) {
                        this.init_echarts(); //初始化图表
                      } else {
                        this.setOption(Chart); //更新数据
                      }
                      var success = res.data.data.success
                      var 　num = 1
                      var list = new Array
                      for (let i = 0; i < predict.length; i++) {
                        var value = predict[i]
                        list.push(value)
                        Math.max(...list)
                        //判断数字出现的概率
                        this.refrain(list)
                      }

                      var success = res.data.data.success
                   
                      this.setData({
                        success,
                        predict,
                        num: num++
                      })
                    })
                  })

                })

              }
            })

          }
        })
      }
    })
  },
  cz(){
    wx.clearStorage('number')
    wx.showToast({
      title: '重置成功',
    })
  },
  black(){
    wx.switchTab({
      url: '/pages/index/index',
    })
  },
  setOption: function (Chart) {
    Chart.clear();  // 清除
    Chart.setOption(this.getOption());  //获取新数据
  },
  // 图表配置项
  getOption() {
    var self = this;
    var option = {
      title: {//标题
        text: '轴承数据',
        left: 'center'
      },
      renderAsImage: true, //支持渲染为图片模式
      color: ["#FFC34F", "#FF6D60", "#44B2FB"],//图例图标颜色
      legend: {
        show: true,
        itemGap: 25,//每个图例间的间隔
        top: 30,
        x: 30,//水平安放位置,离容器左侧的距离  'left'
        z: 100,
        textStyle: {
          color: '#383838'
        },
        data: [//图例具体内容
          {
            name: '正常',//图例名字
            textStyle: {//图例文本样式
              fontSize: 13,
              color: '#383838'
            },
            icon: 'roundRect'//图例项的 icon，可以是图片
          },
          {
            name: '内圈',
            textStyle: {
              fontSize: 13,
              color: '#383838'
            },
            icon: 'roundRect'
          },
          {
            name: '外圈',
            textStyle: {
              fontSize: 13,
              color: '#383838'
            },
            icon: 'roundRect'
          }
        ]
      },
      grid: {//网格
        left: 30,
        top: 100,
        containLabel: true,//grid 区域是否包含坐标轴的刻度标签
      },
      xAxis: {//横坐标
        type: 'category',
        name: '',//横坐标名称
        nameTextStyle: {//在name值存在下，设置name的样式
          color: 'red',
          fontStyle: 'normal'
        },
        nameLocation: 'end',
        splitLine: {//坐标轴在 grid 区域中的分隔线。
          show: true,
          lineStyle: {
            type: 'dashed'
          }
        },
        boundaryGap: false,//1.true 数据点在2个刻度直接  2.fals 数据点在分割线上，即刻度值上
        data: ['1', '2', '3',  '时间'],
        axisLabel: {
          textStyle: {
            fontSize: 13,
            color: '#5D5D5D'
          }
        }
      },
      yAxis: {//纵坐标
        type: 'value',
        position: 'left',
        name: '工作参数',//纵坐标名称
        nameTextStyle: {//在name值存在下，设置name的样式
          color: 'red',
          fontStyle: 'normal'
        },
        splitNumber: 5,//坐标轴的分割段数
        splitLine: {//坐标轴在 grid 区域中的分隔线。
          show: true,
          lineStyle: {
            type: 'dashed'
          }
        },
        axisLabel: {//坐标轴刻度标签
          formatter: function (value) {
            var xLable = [];
            if (value == 20) {
              xLable.push('驱动端');
            }
            if (value == 40) {
              xLable.push('风扇端');
            }
            if (value == 60) {
              xLable.push('加速度');
            }
            if (value == 80) {
              xLable.push('转速');
            }
            // if (value == 100) {
            //   xLable.push('偏航位置');
            // }
            return xLable
          },
          textStyle: {
            fontSize: 13,
            color: '#5D5D5D',
          }
        },
        min: 0,
        max: 100,
      },
      series: [{
        name: '',
        type: 'line',
        data: [0, 20, 30, 40, 50, 60, 70],
        symbol: 'none',
        itemStyle: {
          normal: {
            lineStyle: {
              color: '#FFC34F'
            }
          }
        }
      }, {
        name: '',
        type: 'line',
        data: [20, 30, 80, 50, 60,10, 80],
        symbol: 'none',
        itemStyle: {
          normal: {
            lineStyle: {
              color: '#FF6D60'
            }
          }
        }
      }, {
        name: '',
        type: 'line',
        data: [30, 70, 20, 80, 30, 90, 70],
        symbol: 'none',
        itemStyle: {
          normal: {
            lineStyle: {
              color: '#44B2FB'
            }
          }
        }
      }],
    }
    return option;
  },
});

