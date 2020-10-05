function Add_Class() {
    this.navLink = $('.nav-link');
    this.hasTreeView = $('.has-treeview');
}

Add_Class.prototype.listenClassEvent = function(node, _class) {
    if (location.href.split('?')[0] === node.href) {
        $(node).addClass(_class);
        $(node).parents('.has-treeview').addClass('menu-open');
        $(node).parents('.has-treeview').children('.nav-link').addClass('active');
    }
};

Add_Class.prototype.addActiveEvent = function (){
    var self = this;
    self.hasTreeView.each(function () {
        var selfHasTree = $(this);
        self.listenClassEvent(selfHasTree.find('.nav-link'), 'active');
    })
    self.navLink.each(function () {
        if (!this.classList.contains('active')) {
            self.listenClassEvent(this, 'active');
        }
    });
};


Add_Class.prototype.run = function () {
    this.addActiveEvent();
};

$(function () {
    var add_class = new Add_Class();
    add_class.run();
});