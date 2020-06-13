window.onload = function() {
    if (window.jQuery) {
        // jQuery is loaded
        console.log("jQuery loaded!");
    } else {
        // jQuery is not loaded
        console.log("jQuery failed to load");
    }
}

$(function() {

  $('#topic-select').selectize({
  delimiter: ',',
  persist: false,
  maxItems: null,
  valueField: 'id',
  labelField: 'topic',
  searchField: 'topic',
  options: [
    {id: 1, topic: 'police'},
    {id: 2, topic:'criminal justice system'},
    {id: 3, topic:'prison'}
          ],
  create: false
});

// var resultsTable = $("#test-table").DataTable();

$('#topic-select').on('change input', function(){
    topicArray = {  1 : 'police',
                    2: 'criminal justice',
                    3 : 'prison'  }

    // let topicQueryArr = this.value.map(function(val){
    //   return topicArray[topicValue];
    // })
    let topicQueryArr = JSON.parse("[" + this.value + "]").map(function(val){
      return topicArray[val];
    });
    // console.log(topicQueryArr);
    let topicQueryString = topicQueryArr.join(' ');
    let topicQueryDisplayString = topicQueryArr.join(', ');
    console.log(topicQueryString)
    if(topicQueryString != null && topicQueryString != ''){
      console.log('hi');
      $.ajax({
          url: 'http://trackthechange.co/search/t/'+topicQueryString,
          type: 'GET',
          dataType: 'json',
          success: function(data) {
                                    $("#test-table").show();
                                    var resultsTable = $("#test-table").DataTable({
                                      destroy: true,
                                      data: data,
                                      columnDefs: [
                                        {targets: '_all', className: 'dt-center'},
                                        {targets:0,width:'15%'},
                                        {targets:1,width:'10%'},
                                        {targets:2,width:'15%'},
                                        {targets:3, width:'50%'},
                                        {targets:4, width:'10%'}
                                      ],
                                      columns: [
                                        {title: 'Policy tags', data:null, defaultContent:topicQueryDisplayString},
                                        {title: 'Introduced', data:'introduced_date'},
                                        {title: 'Bill Number', data:'number'},
                                        {title: 'Bill Title', data:'short_title'},
                                        {title: '', data:'bill_slug', render: function(data, type, row, meta){
                                          return '<a href="http://trackthechange.co/bill/'+data+'">Read bill</a>'
                                        }
                                      }
                                      ]
                                    });
                                  },
          error: function(e) { alert('boo!'); console.log(e)}
          // beforeSend: setHeader
            });

        }
        });
// $(document).ready( function () {
//   $('#test-table').DataTable();
});
