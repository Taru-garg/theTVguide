-- Use these functions in your SQL SERVER


-- get all the data except cast for a movie
-- given a mov_id
create procedure Data 
@movID INTEGER
as
	begin
		select 
		movies.mov_id, movies.title, movies.overview,
		movies.initial_release_date, movies.length,
		concat(director.fname, ' ', director.lname) as 'Director',
		ratings.ratings, movieImageData.backdrop, movieImageData.poster,
		genres.genre
		/*count(*)*/
		from movies
		join direction on
		direction.mov_id = movies.mov_id
		join director on
		director.dir_id = direction.dir_id
		join ratings on
		ratings.mov_id = movies.mov_id
		join movieImageData on
		movieImageData.mov_id = movies.mov_id
		join movieGenres on
		movieGenres.mov_id = movies.mov_id
		join genres on
		genres.gen_id = movieGenres.gen_id
		where movies.mov_id = @movID;
	END;
	
	

-- Get all the actors based on a mov_id
create procedure fetchActors
@movId INTEGER
as
	begin
		select cast.mov_id,
		STRING_AGG(concat(actor.fname,' ' ,actor.lname), ', ')
		from [dbo].[CAST]
		join actor on actor.act_id = cast.act_id
		where cast.mov_id = @movId
		group by cast.mov_id;
	end;
	
	
-- Get all actors based on actor name
select cast.mov_id,
STRING_AGG(concat(actor.fname,' ' ,actor.lname), ', ')
from [dbo].[CAST]
join actor on actor.act_id = cast.act_id
where cast.mov_id IN 
	(
		select mov_id from cast where act_id = 
			(
				select act_id from actor where lower(concat(actor.fname, ' ', actor.lname)) = lower('Morgan Freeman')
			)
	)
group by cast.mov_id;



-- Get all data for movies given
-- an actor name
create procedure ActorTOdata 
@movID VARCHAR(40)
as
	begin
		select 
		movies.mov_id, movies.title, movies.overview,
		movies.initial_release_date, movies.length,
		concat(director.fname, ' ', director.lname) as 'Director',
		ratings.ratings, movieImageData.backdrop, movieImageData.poster,
		genres.genre
		/*count(*)*/
		from movies
		join direction on
		direction.mov_id = movies.mov_id
		join director on
		director.dir_id = direction.dir_id
		join ratings on
		ratings.mov_id = movies.mov_id
		join movieImageData on
		movieImageData.mov_id = movies.mov_id
		join movieGenres on
		movieGenres.mov_id = movies.mov_id
		join genres on
		genres.gen_id = movieGenres.gen_id
		where movies.mov_id IN (
		select mov_id from cast where act_id = (
			select act_id from actor where lower(concat(actor.fname, ' ', actor.lname)) = lower('Morgan Freeman')
			)
		);
	END;
	
	
/*select * from [dbo].[MOVIES]
join ratings on
ratings.mov_id = movies.mov_id
where ratings.ratings > 9.0;*/

/* select * from movies
where mov_id in (select cast.mov_id from [dbo].[CAST]
join actor on 
cast.act_id = actor.act_id
where lower(concat(actor.fname, '', actor.lname)) like lower('50%'));
-- or lower(title) like lower('D%')*/

/* Flask SQL Injection
@app.route('/hack/<param>')
def func(param):
    query = f"select * from movies where title='" + param + "'"
    results = conn.processQuerySingle(conn.executeQuery(query, cnxn))
    return results    */


