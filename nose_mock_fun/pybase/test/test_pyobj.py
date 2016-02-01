#!/usr/bin/env python

from pybase.util import pyobj
import mock
from nose import tools as noser

@mock.patch('__builtin__.open')
def pyobj_get_file_contents_test(opener):

    mock_text_array = [ 'this is just a\n',
                        'test\n'
                        ]
    
    opener.return_value.__iter__.side_effect = lambda: iter(mock_text_array)

    
    myPyObj = pyobj.PyObj()
    ret = myPyObj.get_file_contents('/file/doesnt/exist')
    assert opener.called
    noser.assert_equal("".join(mock_text_array), ret)



@mock.patch('__builtin__.open')
def pyobj_get_file_contents_via_context_manager_test(opener):

    mock_text_array = [ 'this is just a\n',
                        'test\n'
                        ]
    
    opener.return_value.__exit__ = mock.Mock(name='file_handle')
    opener.return_value.__enter__.return_value.__iter__.side_effect = lambda: iter(mock_text_array)

        
    myPyObj = pyobj.PyObj()
    ret = myPyObj.get_file_contents_via_context_manager('/file/doesnt/exist')
    assert opener.called
    noser.assert_equal("".join(mock_text_array), ret)


