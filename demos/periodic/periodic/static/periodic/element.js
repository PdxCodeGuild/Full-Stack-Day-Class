'use strict';

function showIonicRadius() {
  console.log('ion');
  $('#ionic-r').show();
  $('#atomic-r').hide();
}

function showAtomicRaidus() {
  console.log('atom');
  $('#atomic-r').show();
  $('#ionic-r').hide();
}

function registerEventHandlers() {
  var raidusLI = $('#r-li');
  raidusLI.on('mouseenter', showIonicRadius);
  raidusLI.on('mouseleave', showAtomicRaidus);
}

$(document).ready(function() {
  registerEventHandlers();
  showAtomicRaidus();
});
