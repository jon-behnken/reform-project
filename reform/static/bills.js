$(function(){

  let billTitle = $('.bill-title');
  let billTitleLength = billTitle[0].innerHTML.length;

  if (billTitleLength > 100){
    $('.bill-title').css('font-size', '18px')
  }

  let billTimelineContainer = $('.timeline')
  for(let i=0;i<billHistory.length;i++){
    let li = document.createElement("li");
    let p = document.createElement("p");

    li.className = 'event'
    p.innerHTML = billHistory[i]['description']

    li.setAttribute('data-date', billHistory[i]['datetime'])
    li.appendChild(p)

    billTimelineContainer.append(li)
  }

});

let sponsorRow = $('.sponsor-row');
for(let s=0;s<billSponsor.length;s++){
  let twitterIcon = document.createElement("img");
  twitterIcon.setAttribute('src', twitterIconUrl);
  twitterIcon.setAttribute('id', 'sponsor-twitter-icon-'+s);

  let writeIcon = document.createElement("img");
  writeIcon.setAttribute('src', writeIconUrl);
  writeIcon.setAttribute('id', 'sponsor-write-icon-'+s);

  let sponsorColumn = document.createElement('div');
  sponsorColumn.className = 'sponsor-column';

  let sponsorCard = document.createElement('div');
  sponsorCard.className = 'sponsor-card';

  let sponsorName = document.createElement("h1");
  sponsorName.innerHTML = billSponsor[s]['sponsor'];

  let sponsorParty = document.createElement("p");
  partyLabel = billSponsor[s]['sponsor_party'];

  let sponsorPhoto = document.createElement("img");
  sponsorPhoto.setAttribute('src', 'https://theunitedstates.io/images/congress/225x275/'+billSponsor[s]['sponsor_id']+'.jpg');

  let contactDiv = document.createElement("div");
  twitterIcon.onclick = function(){
    window.open('https://twitter.com/'+billSponsor[s]['sponsor_twitter'])
  };

  writeIcon.onclick = function(){
    window.open(billSponsor[s]['sponsor_contact_url'])
  };

    contactDiv.appendChild(twitterIcon);
    contactDiv.appendChild(writeIcon);

  if(partyLabel == 'R'){
    partyLabel = 'Republican'
  } else if (partyLabel == 'D'){
    partyLabel = 'Democrat'
  } else {
    partyLabel = 'Other'
  }

  sponsorParty.innerHTML = partyLabel;

  sponsorCard.appendChild(sponsorName);
  sponsorCard.appendChild(sponsorParty);
  sponsorCard.appendChild(sponsorPhoto);
  sponsorCard.appendChild(contactDiv);
  sponsorColumn.appendChild(sponsorCard);

  sponsorRow.append(sponsorColumn);
}

$('#state-select').selectize({
  onChange: function(value){
    $.ajax({
      url: 'http://trackthechange.co/bill/members/all/'+value,
      type: 'GET',
      dataType: 'json',
      success: function(data){
        console.log(data);
        let senatorRow = $('.senator-row');
        senatorRow.empty();

        for(let i=0;i<data.length;i++){
          let twitterIcon = document.createElement("img");
          twitterIcon.setAttribute('src', twitterIconUrl);
          twitterIcon.setAttribute('id', 'twitter-icon-'+i);

          let writeIcon = document.createElement("img");
          writeIcon.setAttribute('src', writeIconUrl);
          writeIcon.setAttribute('id', 'write-icon-'+i);

          let senatorColumn = document.createElement('div');
          senatorColumn.className = 'senator-column';

          let senatorCard = document.createElement('div');
          senatorCard.className = 'senator-card';

          let senatorName = document.createElement("h1");
          senatorName.innerHTML = data[i]['name'];

          let senatorParty = document.createElement("p");
          partyLabel = data[i]['party'];

          let senatorPhoto = document.createElement("img");
          senatorPhoto.setAttribute('src', 'https://theunitedstates.io/images/congress/225x275/'+data[i]['id']+'.jpg');

          let contactDiv = document.createElement("div");
          twitterIcon.onclick = function(){
            window.open('https://twitter.com/'+data[i]['twitter_id'])
          };

          writeIcon.onclick = function(){
            window.open(data[i]['contact_url'])
          };

          contactDiv.appendChild(twitterIcon);
          contactDiv.appendChild(writeIcon);

          if(partyLabel == 'R'){
            partyLabel = 'Republican'
          } else if (partyLabel == 'D'){
            partyLabel = 'Democrat'
          } else {
            partyLabel = 'Other'
          }

          senatorParty.innerHTML = partyLabel;

          senatorCard.appendChild(senatorName);
          senatorCard.appendChild(senatorParty);
          senatorCard.appendChild(senatorPhoto);
          senatorCard.appendChild(contactDiv);
          senatorColumn.appendChild(senatorCard);

          senatorRow.append(senatorColumn);
        }
      }
    });
  }
});




function showActiveTab(t){
  let allTabs = document.querySelectorAll('.'+t.className)
  // console.log(Array.from(allTabs));
  allTabs.forEach(function(i){
    $('#'+i.id).removeClass('active');
  });
  t.className += ' active';

  let activePanelID = t.id.replace('tab', 'pane');
  let activePanel = $('#'+activePanelID);
  $('.bill-data-pane').hide();
  activePanel.show();
}

let allTabsClick = document.querySelectorAll('.bill-sidepanel-tab')
allTabsClick.forEach(function(t){
  $('#'+t.id).on('click', function(){
    showActiveTab(this);
  });
});
