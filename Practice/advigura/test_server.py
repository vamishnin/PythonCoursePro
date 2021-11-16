#!/usr/bin/python

import server_lec13
import unittest
from unittest import mock



class TestServer(unittest.TestCase):
    
    def test_server(self):
        
        srv = server_lec13.TcpServer("127.0.0.1", 5555)
        
        with mock.patch('server_lec13.ClientThread') as client_thread_mock:
            # client_thread_mock.start.return_value = True
            # client_thread_mock.start.side_effect = mock.Mock(side_effect=KeyboardInterrupt())
            
            with mock.patch('socket.socket') as socket_mock:
                socket_impl = mock.MagicMock()                
                socket_impl.accept.return_value = [1, "127.0.0.1"]
                socket_mock.return_value = socket_impl
            
                client_mock = mock.MagicMock()
                client_mock.start.return_value = True
                client_mock.start.side_effect = mock.Mock(side_effect=KeyboardInterrupt())
                client_thread_mock.return_value = client_mock
                
                try:
                    srv.run()
                except KeyboardInterrupt:
                    srv.stop()
                    
                client_thread_mock.assert_called_with(1, "127.0.0.1")
                self.assertTrue(client_mock.start.called)
                
            
if __name__ == '__main__':
    unittest.main()