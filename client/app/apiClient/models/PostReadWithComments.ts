/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { CommentRead } from "./CommentRead";

export type PostReadWithComments = {
    title: string;
    content: string;
    author: string;
    id: number;
    submitted: string;
    edited?: string;
    comments?: Array<CommentRead>;
};
