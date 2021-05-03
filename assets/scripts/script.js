
   class Slider{
   	  constructor(slider){
             this.slider=slider;
              // select all items 
             this.slides=this.slider.querySelector(".slider-items").children;
             // total slides
             this.totalSlides=this.slides.length;
              // getting width of slider container
             this.containerWidth=this.slider.offsetWidth;
             // next slide button
             this.nextSlide=this.slider.querySelector(".next-slide")
             // prev slide button
             this.prevSlide=this.slider.querySelector(".prev-slide")
              // call next slide method
              var that=this;
              this.nextSlide.onclick=function () {
              	that.next()
              }
              // call prev slide method
              this.prevSlide.onclick=function () {
              	that.prev()
              }
              this.index=0;
              this.jumpWidth=0;
             // call setWidth method
             this.setWidth()

   	      // console.log(this.nextSlide);
   	 }
       // set width of all slides items
     setWidth(){
        var totalWidth=0;
         for(let i=0;i<this.slides.length;i++){
         	this.slides[i].style.width=this.containerWidth + "px";
         	totalWidth=totalWidth+this.containerWidth

         }
         // set width of slider-items container
         this.slider.querySelector(".slider-items").style.width=totalWidth + "px";
     }
       // next slide method
     next(){
         if(this.index==this.totalSlides-1){
           this.index=0;
           this.jumpWidth=0;
         }
         else{
         	this.index++;
         	this.jumpWidth=this.jumpWidth+this.containerWidth;
         }
         
        this.slider.querySelector(".slider-items").style.marginLeft=-this.jumpWidth+"px"
     }

     // prev slide method
     prev(){
         if(this.index==0){
           this.index=this.totalSlides-1;
           this.jumpWidth=this.containerWidth*(this.totalSlides-1);
         }
         else{
         	this.index--;
         	this.jumpWidth=this.jumpWidth-this.containerWidth;
         }
         
        this.slider.querySelector(".slider-items").style.marginLeft=-this.jumpWidth+"px"
     }

   }

   const sliderOne=document.querySelector(".slider1");
   const sliderTwo=document.querySelector(".slider2");
   const sliderThree=document.querySelector(".slider3");

  // creating object
  var slider1 =new Slider(sliderOne)
  var slider2 =new Slider(sliderTwo)
  var slider3 =new Slider(sliderThree)









