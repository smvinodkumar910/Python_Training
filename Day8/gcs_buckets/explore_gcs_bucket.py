#!/usr/bin/env python

# Copyright 2019 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License');
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

import sys

# [START storage_list_files]
from google.cloud import storage


def list_blobs():
    """Lists all the blobs in the bucket."""
    #bucket_name = "your-bucket-name"

    storage_client = storage.Client("mynewdevenv")

    #Get all buckets list
    #buckets = list(storage_client.list_buckets())
    #for a in buckets:
    #    print(a.Bucket)

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs("mynewdevenv-bucket")

    # Note: The call returns a response only when the iterator is consumed.
    for blob in blobs:
        print(blob.name)

list_blobs()