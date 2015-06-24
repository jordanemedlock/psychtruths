var colors = ["#FAA","#AFF","#AFA","#FFA", "#FAF","#FC8"];

$(function() {
  $('.tag-btn').each(function(i) {
    $(this).css('background-color',colors[i%colors.length]);
    
  })
})