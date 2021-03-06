# Copyright (C) 2016, 2017 Allen Li
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pathlib

import apsw
import pytest
import sqlalchemy


@pytest.fixture
def tmpdir(tmpdir_factory):
    tmpdir = tmpdir_factory.mktemp('tmpdir')
    return pathlib.Path(str(tmpdir))


@pytest.fixture
def conn():
    return apsw.Connection(':memory:')


@pytest.fixture
def engine():
    return sqlalchemy.create_engine('sqlite:///:memory:')


@pytest.fixture
def aconn(engine):
    return engine.connect()
