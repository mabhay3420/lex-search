import React, { useState } from "react";
import { TextField, Button, Typography, Grid } from "@mui/material";

import VideoPreview from "./VideoPreview";
import { BACKEND_URL } from "./constants";

interface SearchResult {
  chunkInfo: {
    episodeNumber: string;
    chunk: string;
    transcript: {
      start: string;
      end: string;
      content: string;
    };
  };
  episodeInfo: {
    title: string;
    link: string;
  };
}

const SearchPage: React.FC = () => {
  const [searchTerm, setSearchTerm] = useState("");
  const [searchResults, setSearchResults] = useState<SearchResult[]>([]);

  const handleSearch = async () => {
    // perform search using searchTerm
    try {
      const response = await fetch(`${BACKEND_URL}/search/lex?q=${searchTerm}`);
      const data = await response.json();
      // console.log(data);
      console.log(data.data);
      setSearchResults(data.data.result);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <Grid container direction={"column"} spacing={2}>
      <Grid item>
        <Typography variant={"h4"}>Lex Fridman Search</Typography>
      </Grid>
      <Grid item>
        <TextField
          placeholder="Search for a word or phrase"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          //   onKeyDown={handleSearch}
          fullWidth
          sx={{ maxWidth: 500 }}
        />
      </Grid>
      <Grid item>
        <Button onClick={handleSearch} variant={"contained"}>
          Search
        </Button>
      </Grid>
      <Grid item>
        <Grid container direction={"row"} spacing={2}>
          {searchResults.map((result) => (
            <Grid
              key={result.chunkInfo.episodeNumber + result.chunkInfo.chunk}
              item
            >
              <VideoPreview
                key={result.chunkInfo.episodeNumber + result.chunkInfo.chunk}
                title={result.episodeInfo.title}
                description={result.chunkInfo.transcript.content}
                link={result.episodeInfo.link}
              />
            </Grid>
          ))}
        </Grid>
      </Grid>
    </Grid>
  );
};

export default SearchPage;
