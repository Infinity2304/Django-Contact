// app/page.js (Server Component)
import { redirect } from 'next/navigation';
import { cookies } from 'next/headers';

export default function Page() {
  const cookieStore = cookies();
  const authToken = cookieStore.get('user_id');

  console.log('Server Component Running');
  if (authToken) {
    console.log('Token found, redirecting to /home');
    redirect('/home');
  } else {
    console.log('Token not found, redirecting to /login');
    redirect('/login');
  }

  return <p>Redirecting...</p>;
}
