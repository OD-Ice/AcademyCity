function CourseScore() {

}

CourseScore.prototype.listenSubmitEvent = function () {
    var submitBtn = $('.confirm');
    submitBtn.click(function (event) {
        var self = this;
        event.preventDefault();
        var studentIdInput = $(self).parent().siblings()[0];
        var scoreInput = $(self).parent().prev().find('input');
        var studentId = $(studentIdInput).text();
        var score = $(scoreInput).val();
        var courseId = $(self).attr('data-course-id');
        acajax.post({
            'url': '/course/course_score/'+courseId+'/',
            'data': {
                'studentId': studentId,
                'score': score
            },
            'success': function (result) {
                $(self).prop("hidden", "hidden");
            }
        });
    });
};

CourseScore.prototype.run = function () {
    this.listenSubmitEvent();
};

$(function () {
    var courseScore = new CourseScore();
    courseScore.run();
});
