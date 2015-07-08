var colors = ["#FAA","#AFF","#AFA","#FFA", "#FAF","#FC8"];

$(function() {
  $('.tag-btn').each(function(i) {
    $(this).css('background-color',colors[i%colors.length]);
    
  })
  $('a').each(function(i) {
    if ($(this).children().length == 0) {
        var html = $(this).html();
        html = html.replace(/(\/)/gi,'/<wbr>');
        html = html.replace(/(\.)/gi,'.<wbr>');
        $(this).html(html);
    }
  })
})