import { oswald } from "./fonts";

export default function Home() {
    return (
        <main className="mx-auto flex min-h-screen max-w-screen-xl flex-col items-center">
            <h1 className={`${oswald.className} py-24 text-center text-9xl`}>
                Social Thing
            </h1>
            <div className="inline-block rounded border-4 border-cyan-700 px-4 py-2 font-bold text-cyan-500 hover:bg-cyan-700 hover:text-slate-300">
                Go To Feed
            </div>
        </main>
    );
}
