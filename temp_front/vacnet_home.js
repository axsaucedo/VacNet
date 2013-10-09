var screenSize = 0; //Responsive Design
var scrollUp = 0;
var responsiveScreen = {width:window.innerWidth, height:window.innerHeight,
  resizeDetect: function() {
    responsiveScreen.width = window.innerWidth; responsiveScreen.height = window.innerHeight;
    responsiveScreen.cropHeight = 0.4*responsiveScreen.width;
    // if(window.unlockPrompt_on){
    //   lockscreenCanvas.getContext("2d").fillStyle = "rgba(0,0,0,0.7)";
    //   lockscreenCanvas.getContext("2d").fillRect(0,0,lockscreenCanvas.width,lockscreenCanvas.height);
    // }
  },
};

responsiveScreen.resizeDetect();
$("#mainImage").css("width", window.innerWidth);
$("#mainCrop").css("height", responsiveScreen.cropHeight);


/// window.addEventListener("resize", function() { responsiveScreen.resizeDetect(); });
window.onresize = responsiveScreen.resizeDetect;



