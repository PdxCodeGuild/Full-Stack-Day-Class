'use strict';

function getCommentText() {
  return $('#comment-text').val();
}

function appendComment(commentText) {
  var blockquote = $('<blockquote></blockquote>');
  blockquote.text(commentText);
  $('body').append(blockquote);
}

function postCommentText(commentText) {
  var data = {
    'comment_text': commentText
  };
  $.get('/ajax/submit', data, function() {
    appendComment(commentText);
  });
}

function submitComment() {
  var commentText = getCommentText();
  postCommentText(commentText);
}
