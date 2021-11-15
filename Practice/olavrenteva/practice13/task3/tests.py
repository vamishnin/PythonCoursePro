import mock
from class_to_test import TcpServer


class TestTcpServer:
    def test_server_creation(self):
        srv = TcpServer(host='127.0.0.1', port=5555)
        assert srv.host == '127.0.0.1' and srv.port == 5555 and \
               srv._socket is None and not srv._runnning

    @mock.patch('class_to_test.ClientThread')
    @mock.patch('socket.socket')
    def test_server_running(self, socket_mock, cl_thread_mock, capsys):
        srv = TcpServer(host='127.0.0.1', port=5555)

        socket_mock = socket_mock.return_value
        socket_mock.accept.return_value = ('127.0.0.1', 5556)
        cl_thread_mock = cl_thread_mock.return_value
        cl_thread_mock.start.side_effect = [0, KeyboardInterrupt]

        try:
            srv.run()
        except KeyboardInterrupt:
            pass

        captured = capsys.readouterr()

        assert srv._runnning
        assert captured.out.strip() == 'Server is up'
        assert socket_mock.accept.call_count == 2
        assert cl_thread_mock.start.call_count == 2

    def test_server_stop(self, capsys):
        srv = TcpServer(host='127.0.0.1', port=5555)

        srv._socket = mock.Mock()
        srv._runnning = True

        srv.stop()

        captured = capsys.readouterr()

        assert not srv._runnning
        assert captured.out.strip() == 'Server is down'
        assert srv._socket.close.call_count == 1

