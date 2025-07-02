// 封装一个根据屏幕尺寸自动改变 html 的 font-size 大小的函数
const init = function () {
  let clientWidth =
    document.documentElement.clientWidth || document.body.clientWidth;
  // 设计图尺寸是 750px，这样 *20 之后，1rem 就等于 20px;
  const fontSize = (clientWidth / 750 * 20);
  document.documentElement.style.fontSize = fontSize + "px";
};
 
init();
 
window.addEventListener("resize", init);
export default init;