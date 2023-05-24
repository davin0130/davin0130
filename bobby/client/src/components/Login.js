import React from 'react';

class Login extends React.Component {
    render() {
        return (
            <div>
                Bobby Tennis
                <table class="loginForm" method="POST">
                    <tr>
                        <td>ID</td>
                        <td><input name="id"></input></td>
                    </tr>
                    <tr>
                        <td>PW</td>
                        <td><input name="pw"></input></td>
                    </tr>
                    <tr>
                        <td><input type="submit" value="로그인"></input></td>
                    </tr>
                </table>
            </div>
        )
    }
}

export default Login;