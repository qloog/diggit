# -*- coding: utf-8 -*-

import pytest
from framework import DiggitTestCase
from model.user import User


@pytest.fixture
def add_user(request):
    name = 'unittest1'
    email = 'unittest1@gmail.com'
    city = 'Beijing'
    blog = 'http://daydayfree.github.io'
    intro = 'I am a unittest!'
    uid = 'unittest1'
    user = User.new(name, email, city, blog, intro, uid)
    self = request.instance
    self.user = user
    return user


@pytest.mark.usefixtures("add_user")
class DiggitUserTestCase(DiggitTestCase):

    def test_can_add_a_new_user(self):
        name = 'unittest1'
        email = 'unittest1@gmail.com'
        city = 'Beijing'
        blog = 'http://daydayfree.github.io'
        intro = 'I am a unittest!'
        uid = 'unittest1'
        new = User.new(name, email, city, blog, intro, uid)
        assert new
        assert new.name == name
        assert new.email == email
        assert new.city == city
        assert new.blog == blog
        assert new.intro == new.intro
        assert new.uid == uid

    def test_can_update_user_intro(self):
        user = User.get_by_uid(self.user.uid)
        assert user
        intro = 'I am a unittest (modified)'
        new = user.update(intro=intro)
        assert new
        assert new.intro == intro


