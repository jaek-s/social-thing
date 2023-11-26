/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { CommentCreate } from "../models/CommentCreate";
import type { CommentRead } from "../models/CommentRead";
import type { CommentUpdate } from "../models/CommentUpdate";

import type { CancelablePromise } from "../core/CancelablePromise";
import { OpenAPI } from "../core/OpenAPI";
import { request as __request } from "../core/request";

export class CommentsService {
    /**
     * Get Comment List
     * @param postId
     * @param offset
     * @param limit
     * @returns CommentRead Successful Response
     * @throws ApiError
     */
    public static commentsGetCommentList(
        postId: number,
        offset?: number,
        limit: number = 25,
    ): CancelablePromise<Array<CommentRead>> {
        return __request(OpenAPI, {
            method: "GET",
            url: "/posts/{post_id}/comments",
            path: {
                post_id: postId,
            },
            query: {
                offset: offset,
                limit: limit,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Create Comment
     * @param postId
     * @param requestBody
     * @returns CommentRead Successful Response
     * @throws ApiError
     */
    public static commentsCreateComment(
        postId: number,
        requestBody: CommentCreate,
    ): CancelablePromise<CommentRead> {
        return __request(OpenAPI, {
            method: "POST",
            url: "/posts/{post_id}/comments",
            path: {
                post_id: postId,
            },
            body: requestBody,
            mediaType: "application/json",
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Get Comment
     * @param commentId
     * @param postId
     * @returns CommentRead Successful Response
     * @throws ApiError
     */
    public static commentsGetComment(
        commentId: string,
        postId: number,
    ): CancelablePromise<CommentRead> {
        return __request(OpenAPI, {
            method: "GET",
            url: "/posts/{post_id}/comments/{comment_id}",
            path: {
                comment_id: commentId,
                post_id: postId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Delete Comment
     * @param commentId
     * @param postId
     * @returns void
     * @throws ApiError
     */
    public static commentsDeleteComment(
        commentId: string,
        postId: number,
    ): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: "DELETE",
            url: "/posts/{post_id}/comments/{comment_id}",
            path: {
                comment_id: commentId,
                post_id: postId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Edit Comment
     * @param commentId
     * @param postId
     * @param requestBody
     * @returns any Successful Response
     * @throws ApiError
     */
    public static commentsEditComment(
        commentId: string,
        postId: number,
        requestBody: CommentUpdate,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: "PATCH",
            url: "/posts/{post_id}/comments/{comment_id}",
            path: {
                comment_id: commentId,
                post_id: postId,
            },
            body: requestBody,
            mediaType: "application/json",
            errors: {
                422: `Validation Error`,
            },
        });
    }
}
